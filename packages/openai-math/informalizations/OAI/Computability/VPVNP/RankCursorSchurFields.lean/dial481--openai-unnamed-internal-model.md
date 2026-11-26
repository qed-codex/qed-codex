---
{
  "module": "OAI/Computability/VPVNP/RankCursorSchurFields.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCursorSchurFields.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCursorSchurFields.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Loading the six Schur root fields from the rank cursor

The product root consists of its zero tag, balanced-product depth, zero
block start, matrix row count and the two cursor indices. The loader copies
these six words from the cursor bank into the live query frame, preserving
all input registers. The matrix dimensions and both degrees are stack data.


### `loadRoot`

 Copy the product tag, depth, block start, row count, and two scan indices into the six
fields of the Schur root request. 

### `loadClock`

 Step bound for the six copies of w-bit words that initialize a Schur root request. 

### `loadRoot_runs`

 Normal return puts the engine directly at its typed root-entry bank, with
the input registers, descriptor bank and empty scratch preserved. 
