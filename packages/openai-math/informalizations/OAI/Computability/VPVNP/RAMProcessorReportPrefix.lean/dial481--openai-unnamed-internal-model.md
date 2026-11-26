---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorReportPrefix.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorReportPrefix.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorReportPrefix.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Returning a private event prefix from a physical call segment

The internal instruction scan contributes ticks and private branch choices to
the report. Its prefix consumes no external probes, so it leaves the costs,
record timestamps, and emitted slots of the external continuation intact.


### `Report.withEvents`

 Prepend an ordered event prefix to a call report and retain its final result. 

### `allowance`

 Number of further probes admitted by all three budgets, the minimum of the remaining call,
global and site credits. 
