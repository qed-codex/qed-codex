---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorProbeCredit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorProbeCredit.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorProbeCredit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Charged probe entry and post-emission timestamps

Startup and every external probe enter the same precharge. A successful
precharge preserves the saved call start and current ordinal. Emission can
therefore read them before the separate ordinal increment.


### `prepareProbe`

 Charge a probe against call, site and global credit, and increment the cumulative cost. An
exhausted allowance or cost overflow rejects before the probe is staged. 

### `prepareProbe_reject`

 Failed precharging updates only budget ports and cannot reach a probe
callback. The controls are physically at the rejecting halt. 

### `withProbe`

 Run the record callback after paying for the probe and before increasing
its ordinal. The callback may use the saved timestamp words and may update
the surrounding record buffers. 
