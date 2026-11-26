---
{
  "module": "src/Lib/Base.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Base.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Base.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The adjoint of a matrix for the Hermitian dot product

The other files of `Lib` and `New`, except `Lib.Speed`, import this file, directly or not, and
with it the speed settings of `Lib.Speed`.


### `star_mulVec_dotProduct`

 `Bᴴ` is the adjoint of `B` for the standard Hermitian form. 
