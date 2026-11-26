---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkPrefixCharge.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkPrefixCharge.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkPrefixCharge.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Traffic of the first thirty-six scheduled shrinking rows

The three header reports have a fixed charge. The greedy, placement,
bundle, term, and chosen-geometry workers use a bounded number of calls
and probes per old position. For the installed geometry group the two
score cursor conventions give the same events and number of calls.


### `fixedHeaderRate`

 Total calls and probes for the three header publications of this shrinking substep. 

### `fixedHeaderCap`

 Bound on one header report's event count plus the final instruction, used for private fuel. 

### `prefixRate`

 Per-old-position traffic coefficient for the first 36 shrinking visits, combining header
publication with the selected graph, term and geometry scans. 

### `raw_charge`

 Charge and clock of each actual source call, including all three
fixed header rows on the live input memories. 

### `group_charge`

 Apply the exact report and tape identities returned by the twenty-two
preparation and selection rows and the fourteen chosen-geometry rows. 

### `group_tick_bound`

 Each actual scheduled source report obeys the clock proved for its
catalog occurrence, including the redirected score reports. 
