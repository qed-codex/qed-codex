---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpFieldTableEnumeration.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpFieldTableEnumeration.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpFieldTableEnumeration.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Actual enumeration of a clause's local field table

The callback is the concrete preserving field-row program. The loop visits a
scalar interval and emits one Boolean value per rank, so the output order is
descending rank and each rank is interpreted with least-significant base-p
coordinate first. All costs include the growing number of local rows.


### `callbackBound`

 A deliberately explicit bound polynomial in the row count and descriptor
sizes; the rank width is bounded by the number of executed increments. 

### `body_step`

 The quantified callback premise is closed with the concrete row program. 

### `enumerate_runsIn`

 Complete table enumeration with explicitly supplied binary fuel. The fuel
is tied to p^arity by `table_runsIn`; setup is an actual separate program. 

### `table_runsIn`

 The table has exactly p^arity rows, with no enumeration of all D labels. 

### `enumerationBound`

 A closed allowance when the supplied fuel has a known word-width bound.
The local row count remains explicit in both the callback and loop costs. 
