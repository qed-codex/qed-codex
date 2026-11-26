---
{
  "module": "OAI/Computability/VPVNP/SliceGeometryPencil.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceGeometryPencil.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceGeometryPencil.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exceptional parameters for matrices of affine polynomials

A maximal-rank specialization supplies a nonzero minor. Its determinant
remains nonzero off at most one exceptional scalar per column, because the
matrix entries have degree at most one. Comparing two such ranks therefore
gives a bounded or cobounded parameter set.


### `exists_generic_rank`

 The rank is constant away from at most `#J` parameters. This also covers
empty matrices and finite fields. 

### `boundedOrCobounded_rank_lt`

 The strict rank comparison of two affine polynomial matrices with the same
column type holds at finitely many parameters or at all but finitely many. 
