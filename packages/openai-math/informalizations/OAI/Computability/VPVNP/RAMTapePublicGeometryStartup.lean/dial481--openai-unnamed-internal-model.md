---
{
  "module": "OAI/Computability/VPVNP/RAMTapePublicGeometryStartup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapePublicGeometryStartup.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapePublicGeometryStartup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Public-expression registers initialized from the original site tape

The record startup first parses the physical input and prepares its public
processor fields. The next finite routine forms the four fixed-width
arithmetic inputs. Its quadratic preparation cost fits the existing startup
clock for all lengths and sites satisfying the processor input bound.


### `startup`

 Parse the raw site and prepare its initial-record words, then convert the geometry tallies
and initialize the arithmetic registers. 

### `startup_runs`

 The fixed public arithmetic register bank is ready after parsing an
actual complete processor input, with every original public stack retained. 
