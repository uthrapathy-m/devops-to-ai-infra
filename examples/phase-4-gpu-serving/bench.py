import asyncio, json, statistics, time
import httpx

URL = "http://localhost:8000/v1/chat/completions"   # kubectl port-forward svc/vllm-qwen 8000
MODEL = "Qwen/Qwen2.5-7B-Instruct-AWQ"
PROMPT = "Explain Kubernetes taints and tolerations in 150 words."


async def one_request(client):
    body = {"model": MODEL, "messages": [{"role": "user", "content": PROMPT}],
            "max_tokens": 256, "stream": True}
    start, ttft, tokens = time.perf_counter(), None, 0
    async with client.stream("POST", URL, json=body) as resp:
        async for line in resp.aiter_lines():
            if not line.startswith("data: ") or line.endswith("[DONE]"):
                continue
            chunk = json.loads(line[6:])
            if chunk["choices"] and chunk["choices"][0]["delta"].get("content"):
                ttft = ttft or time.perf_counter() - start
                tokens += 1                     # approx: one streamed chunk = one token
    return ttft, tokens


async def run(concurrency, total=64):
    sem = asyncio.Semaphore(concurrency)
    async with httpx.AsyncClient(timeout=180) as client:
        async def guarded():
            async with sem:
                return await one_request(client)
        t0 = time.perf_counter()
        results = await asyncio.gather(*[guarded() for _ in range(total)])
        wall = time.perf_counter() - t0
    ttfts = sorted(r[0] for r in results if r[0])
    tok_s = sum(r[1] for r in results) / wall
    p95 = ttfts[int(0.95 * (len(ttfts) - 1))]
    print(f"c={concurrency:>3}  {tok_s:7.1f} tok/s  TTFT p50={statistics.median(ttfts):.2f}s  p95={p95:.2f}s")


for c in (1, 8, 32):
    asyncio.run(run(c))
