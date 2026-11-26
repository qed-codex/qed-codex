---
{
  "module": "OAI/Computability/VPVNP/CouplingAmplification.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CouplingAmplification.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CouplingAmplification.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Amplification of the endpoint-coupling estimate

Appendix A.3 of *VP and VNP differ over every field* bounds a wire value by a
binary tree of exterior decompositions. The finite exterior level estimate
controls each child's table with no asymptotic error. After summing the leaves,
the wire dimension tends to infinity at fixed depth, and then the depth tends
to infinity.


### `couplingLevel`

 Exterior level used for a split with wire length `t` and current endpoint exponents `N`. 

### `couplingLevel_bounds`

 At the chosen level both normalized crossing factors obey their target bounds for
each finite wire dimension `q ≥ 2`. 

### `split_endpoint_bounds`

 The normalized endpoint bounds at both children of an Appendix A.3 split. 

### `leafTable_append_child`

 The cost table at an appended child agrees with one more split of the current table. 

### `endpoint_tree_bounds`

 Propagating normalized endpoint estimates from the root to any path of the given depth. 

### `normalized_endpoint_product_bound`

 The independent endpoint estimate (A.4) passes to normalized values because
its exponents sum to one. Applies to any coupling with these marginals. 

### `binary_tree_bound`

 A depth-`a` tree with subadditive parent values and uniformly bounded leaf values. 

### `coupling_tree_bound`

 The root is at most `2 ^ a` times the common coupling bound for the leaves. 

### `le_of_dyadic_amplification`

 A fixed dyadic prefactor vanishes from the exponential rate as the power tends to infinity.
The remaining error tends to zero as the precision index increases. 
