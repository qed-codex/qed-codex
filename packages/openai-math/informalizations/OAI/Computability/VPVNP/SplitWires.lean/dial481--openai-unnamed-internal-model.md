---
{
  "module": "OAI/Computability/VPVNP/SplitWires.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SplitWires.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SplitWires.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Contraction of a split pair of wires

In the first case of Theorem 2.4 of *VP and VNP differ over every field*,
the added party is the common endpoint of two bundles of binary wires.
Contracting with one covector gives a rectangular matrix on the old parties.
The identity covector on equal-size bundles recovers the old equality wire.


### `splitWires`

 Two wire bundles with a common new endpoint and outside endpoints `a` and `b`. 

### `splitCenterEquiv`

 The center keeps one independent index for each bundle. 

### `splitLeafEquiv`

 The old legs keep just the corresponding outside endpoint indices. 

### `splitMatrix`

 In endpoint bases a covector is a rectangular matrix of independent entries. 

### `contractCenter_splitWires_coeff`

 Exact readout of the matrix supplied by the center covector. 

### `wire_power_mutual`

 A tensor power of an equality wire is one wire whose index is the tuple
of the individual edge indices. 

### `binarySplit`

 The split monomial before regrouping the parallel binary factors. 

### `binary_splitWires_mutual`

 Regrouping powers of two binary wires into the two dyadic bundles. 

### `splitWires_matrix_mutual`

 Contraction gives exactly the matrix tensor after local basis changes at the leaves. 

### `exists_splitWires_matrix`

 Conversely every matrix on the two outside endpoints occurs as a center contraction. 

### `embedOld_wire_mutual`

 Embedding an old wire preserves both endpoint bases and adds a trivial
factor at the center. This identifies old and enlarged wire values. 

### `rank_splitMatrix_le`

 Rank bound for the contraction matrix of the two dyadic bundles. 

### `wireDistance_extension`

 An extension on all old tensors restricts to the original wire pseudometric
at every pair of old parties. 

### `value_splitWires_le_min`

 The contracted value is bounded by the wire with the smaller dimension. 

### `value_splitWires_le`

 Every joint center covector obeys the split target for arbitrary prescribed
nonnegative lengths whose sum equals the old wire distance. 

### `exists_splitWires_value_eq`

 With equal bundle widths the identity covector attains the split target. 

### `value_binarySplit_monomial_le`

 The same bound for a monomial in the original binary wire generators times any
embedded old tensor. The covector can couple all binary indices. 

### `exists_binarySplit_monomial_eq`

 Equal multiplicities attain the monomial target, with the embedded old factor
passing through the contraction. 

### `contractionValue_binarySplit_monomial_le`

 The upper bound holds for the supremum of all joint contractions. 

### `contractionValue_binarySplit_monomial_eq`

 The supremum for equal multiplicities is the target itself. 

### `ofTensor_binarySplit`

 On restriction classes the two bundles are the corresponding monomial
in the two added generators. 
