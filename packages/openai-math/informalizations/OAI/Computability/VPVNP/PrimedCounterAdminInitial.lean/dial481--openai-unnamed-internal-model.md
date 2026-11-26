---
{
  "module": "OAI/Computability/VPVNP/PrimedCounterAdminInitial.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterAdminInitial.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterAdminInitial.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Initial parser state after the primed input passes

The parser's input rectangle is the output of the second pass. Its stack,
marks and production counters begin immediately beyond that rectangle. The
prescribed header memory initializes these scratch cells to zero and stores
the nominated histogram before the first-pass rectangle.


### `assembled_nomination`

 Each nomination word remains available at the prescribed histogram offset. 

### `assembled_holds`

 After both passes the pending list, marks and accumulated histogram are empty,
while every terminal read already sees its prescribed input bit. 
