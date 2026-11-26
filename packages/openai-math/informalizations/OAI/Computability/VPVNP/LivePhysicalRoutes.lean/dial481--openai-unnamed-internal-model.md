---
{
  "module": "OAI/Computability/VPVNP/LivePhysicalRoutes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LivePhysicalRoutes.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LivePhysicalRoutes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Physical header path equivalences for pair and evaluator groups

The same code recovers the actual literals and cut payloads and decides the
mode. At a valid active group the entire choice-free prefix is forced on
every accepting path. Its continuation begins at nomination or at the
first-tail test, with the checked payloads in their physical memory banks.


### `PrefixTrace`

 A checked finite prefix ending at a named outer stage. 

### `PrefixTrace.logs`

 Chronological reports of the deterministic header calls that reach the stated outer
  stage. 

### `equiv`

 Every accepting path from the original physical memory has exactly these
header bursts. The predicate on the remaining path accounts for their cost. 

### `valid_prefix_equiv`

 The deterministic physical prefix up to the mode router, with the exact
header image that the three subsequent cases consume. 

### `ActiveMode`

 The two modes in which a checked group continues computation, either counting a primed pair
or checking an evaluator transition. 

### `ActiveMode.tag`

 The header mode tag for the active pair or evaluator-tail branch. 

### `ActiveMode.flag`

 Numeric flag read by the mode router, one for a pair group and two for an evaluator-tail
group. 

### `ActiveMode.stage`

 First continuation after the mode router, the nomination stage for a pair or the first-tail
test for an evaluator group. 

### `active_prefix`

 Start the actual nominated pair computation or the evaluator-tail
computation, after the header and mode router have both run. 
