---
{
  "module": "OAI/Computability/VPVNP/DegreeRefresh.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/DegreeRefresh.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/DegreeRefresh.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Energy of the degree-restoring step

Section 7.3 of *VP and VNP differ over every field* concatenates all the old
wires over one base arc and replaces the segment ties in each block of ports
by a term of a fixed expander motif. There are two internal ties per ordered
pair of distinct ports. The external widths cost at most `d₀ L`; across all
blocks the internal demands cost at most `2 L`. The comparison constant
`2 γ d₀ / dH` for the metric motif is independent of the order of the block.


### `Tie`

 The two copies distinguish the incoming and outgoing ties between ports. 

### `Widths`

 Old wires indexed in source-port order, before their concatenation. 

### `incoming`

 The width found at a destination block, incoming slot and destination port. 

### `tieWidth`

 In either direction the first port carries the old half-wire; the second
is the designated slot at which its segment of the external wire is read. 

### `oldEnergy`

 Squared-width energy of the old network. 

### `externalEnergy`

 Squared-width energy of the concatenated external payloads. 

### `demandEnergy`

 The energy of the two sets of nonlocal segment ties in a block. 

### `oldEnergy_incoming`

 Reindexing the old energy at its incoming half-wires counts every width once. 

### `demandEnergy_sum_le`

 All internal ties together cost at most the old energy counted twice. Ties
at the same port are local and may be omitted even if their widths are positive. 

### `externalEnergy_le`

 Cauchy–Schwarz bounds the external energy after concatenating the `D`
segments of each bundle, using `D p = d₀ p'`. 

### `metric_comparison`

 The metric hypothesis of the expander motif in Section 7.3, with the actual
directed arcs as supply and two copies of the off-diagonal as demand. 

### `refresh_energy_le`

 Summing the termwise energy inequality of Theorem 6.1 over all blocks
gives Equation (7.3). The additive term is exactly `C · P²` when the motif's
scaled additive constant is `C` and `P = #blocks · D`. 
