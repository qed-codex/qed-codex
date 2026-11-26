---
{
  "module": "OAI/Computability/VPVNP/ParseIncidence.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ParseIncidence.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ParseIncidence.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Reconstructing ordered parses from their incidence tables

Starting at a selected event, follow the two child requests to build a parse. Child
layers decrease strictly. Conversely, every selected event has a chain of parents
ending at the root. This rules out disconnected selections and makes the encoding
parsimonious.


### `eq_of_valid_subset`

 If two locally valid tables have the same root and one is contained in the other,
they coincide. Ascending parent links ends at the root because the table is finite. 

### `IsParseTable.existsUnique_parse`

 Local incidence tests give exactly one ordered parse, with one event for each
terminal or binary production occurrence. 
