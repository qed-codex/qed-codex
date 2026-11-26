---
{
  "module": "OAI/Computability/VPVNP/NetworkKernel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/NetworkKernel.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/NetworkKernel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Placed local kernels of a wire network

Equation (7.1) of *VP and VNP differ over every field* sums over motif choices
and then over one shared assignment per edge of the chosen output network.
A choice determines the topology, the widths, and the placement of whole old
vertex factors. Contracting the expansion against arbitrary factors only
requires independent old half-wire indices inside each new site.


### `Network`

 An indexed wire network. The payload alphabet can vary from edge to edge. 

### `Network.Site`

 Finite type of sites where the network's half-wire payloads are assigned. 

### `Network.Edge`

 Finite type of individual directed wires whose endpoint payloads are equated by the
  network tensor. 

### `Network.src`

 Source site of a directed wire, where its outgoing half-wire payload is assigned. 

### `Network.dst`

 Destination site of a directed wire, where its incoming half-wire payload is assigned. 

### `Network.Payload`

 Finite alphabet of possible payloads shared by the two ends of each wire. 

### `Network.Half`

 Independent assignments to all incoming and outgoing half-wires at a site. 

### `Network.tensor`

 The equality of the two half-wire indices on each edge. 

### `Network.coeff`

 Product of wire equality indicators on a global half-wire assignment. 

### `Placed`

 Local old indices assigned to a single new site by the placement. 

### `Term`

 One admitted term of a substep. Its network and placement can depend on
the entire list of selected motif terms. 

### `Term.output`

 New network used in this summand of the compression step. 

### `Term.place`

 Assigns each old site to the new site that receives its half-wire data. 

### `Term.kernel`

 Local coefficient at a new site, depending on the old half-wire data placed there and on
  the new half-wire assignment. 

### `Term.value`

 Wire expansion in one term, read as a local map on the output wire tensor. 

### `Term.value_eq_edgeSum`

 Each term of (7.1) uses exactly one sum per new edge, including parallel
edges. Both ends of the edge use the same payload. 

### `Step`

 A substep specifies its finite term list and the coefficient identity. 

### `Step.Choice`

 Finite index type of terms in the exact expansion of the old network's coefficient. 

### `Step.term`

 Output network, placement and local kernels chosen by a term index. 

### `Step.edgeExpansion`

 Equation (7.1), with both sums and the dependence of all incidence data on
the chosen term displayed. 

### `Factors`

 Whole local factors, evaluated at a fixed choice of any external indices. 

### `contract`

 Contract the wire equalities with arbitrary local factors. 

### `contract_edgeSum`

 In a contraction against wire equalities, one common value per edge
suffices. 

### `Term.placedProduct`

 Only the original factors placed at this site enter its local product. 

### `Term.push`

 The new local vertex factor obtained by summing the old half-wire indices
at this site. The same kernel applies when the old factors carry free indices. 

### `Term.contract_value`

 A single placed kernel contracts locally against the complete old factors. 

### `Step.contract_eq_sum`

 Substitution of a kernel expansion preserves the contraction of an
arbitrary old network over the coefficient semiring. 

### `Term.pushOpen`

 Push an old factor with external indices, carrying all of those indices
to its designated new site. The local map only reads the external indices
in that site's placement fiber. 

### `Step.contract_open`

 Substep substitution with uncontracted indices. At each new site the
external input consists exactly of the old external inputs placed there. 

### `Layout`

 A layout before contraction of wires whose two endpoints land at the
same output site. Each of these wires has one payload, owned by that site. 

### `Layout.output`

 Network of exposed wires remaining after internal labels are summed. 

### `Layout.place`

 Assigns each old site to the output site at which its data enter the local coefficient. 

### `Layout.Internal`

 Finite type of absorbed wires or other internal summation indices. 

### `Layout.Label`

 Finite alphabet summed over at each internal index. 

### `Layout.owner`

 Output site responsible for summing the label at each internal index. 

### `Layout.entry`

 Local coefficient before summation, depending on the old data placed at the site, its
  internal labels and its exposed half-wires. 

### `Layout.term`

 Summing each absorbed edge once, inside the kernel at its owner. 

### `Layout.term_value`

 Local sums over internal wires are equal to one global assignment to the
internal wires. The shared edge indices of the output are summed separately. 

### `Step.ofMotifProduct`

 Assemble exact motif expansions into a step of (7.1). The hypotheses
describe the original demand factorization, the individual motif identities,
and the two properties of the selected layout: its payload bijection and
the regrouping of its map entries. The layout may depend on the whole list
of selectors. 

### `Term.value_eq_contract`

 Fixing the old half-wire indices turns a term into a contraction of the
new network against the rows of its local kernels. 

### `History`

 Finite branch-dependent iteration of substeps. A branch can use a
different continuation for each selected term. 

### `Path`

 Fully enumerated paths carry every term choice, each old half-wire
assignment separately, and the one shared final payload on each final edge. 

### `weight`

 Product of original factor entries and the kernel entries selected by the
path. Every intermediate assignment is explicitly part of the path. 

### `contract_eq_sum_paths`

 Iterated substitution as a single finite sum over fully expanded paths.
This is the exact algebra used before weighting paths in Section 12. 
