---
{
  "module": "OAI/Computability/VPVNP/LiveProgramPair.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramPair.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramPair.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The four ordinary handoffs before the first-half exponent check

Histograms and accepted compressor choices remain separate indices. The
initializer and copy have one path each. Joining the four stages preserves
the entire report sequence that enters the final exponent check.


### `Chronology`

 Local path classifications of the four stages preceding the terminal
digit test. Each classification concerns only its native component. 

### `Chronology.nominations`

 Nomination-stage histories starting in the group’s initial memory and indexed by the
  chosen histogram. 

### `Chronology.init`

 The unique auxiliary initialization following each nomination in the memory left by that
  nomination. 

### `Chronology.copy`

 The unique auxiliary copy following initialization for the chosen nomination. 

### `Chronology.pair`

 Pair-stage histories starting in the copy’s actual final memory and indexed by a path for
  that nomination. 

### `prefixLogs`

 Linked reports from nomination, initialization, sparse copy, and the selected pair path
concatenated in execution order. 

### `paths`

 Every accepting run through this branch has one and only one nomination,
one compressed pair path, and one accepting terminal check. The final check's
cap includes the reports of all four preceding stages. 
