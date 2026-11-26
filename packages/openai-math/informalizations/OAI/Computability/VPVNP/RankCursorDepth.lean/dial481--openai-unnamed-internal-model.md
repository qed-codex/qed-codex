---
{
  "module": "OAI/Computability/VPVNP/RankCursorDepth.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCursorDepth.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCursorDepth.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Preparing the depth of the Schur product from a binary matrix dimension

At startup the dimension is present on the row-count stack. The rank scan
copies it into the depth word, then computes its ceiling binary logarithm.
The one-register logarithm uses the cursor's otherwise empty ISA work
stacks and leaves every cursor register available to the first request.


### `prepareDepth`

 Copy the binary row count to the depth stack and replace the copy by its ceiling base-two
logarithm. 

### `depthClock`

 Step bound for copying a w-bit row count and computing the depth of the balanced Schur
product. 

### `prepareDepth_runs`

 At normal return the bank contains the computed depth word for the full
rank scan. This also works for dimension zero and for the empty word. 

### `prepareDepth_bounded`

 The startup space is polynomial in word width, with the incoming
engine storage and any previously supplied flag bits counted separately. 
