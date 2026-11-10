helm install llm-gateway oci://ghcr.io/berriai/litellm-helm \
  --namespace ai-gateway --create-namespace -f values.yaml

# one key per team: budget in USD, reset every 30 days, 120 requests/min
curl -s https://llm-gateway.internal/key/generate \
  -H "Authorization: Bearer $LITELLM_MASTER_KEY" \
  -H "Content-Type: application/json" \
  -d '{"team_id": "support-bot", "max_budget": 200, "budget_duration": "30d", "rpm_limit": 120}'
