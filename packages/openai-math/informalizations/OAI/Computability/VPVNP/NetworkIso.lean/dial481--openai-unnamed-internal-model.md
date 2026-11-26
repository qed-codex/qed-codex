---
{
  "module": "OAI/Computability/VPVNP/NetworkIso.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/NetworkIso.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/NetworkIso.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Relabelling a placed wire-network expansion

Bijections on sites, edges and individual payload alphabets preserve each
wire equality. Transporting both the input and a choice-dependent output
therefore preserves the exact identity for a substep.


### `Network.Iso`

 A relabelling of sites and edges, with a bijection on the alphabet of each wire. 

### `Network.Iso.site`

 Bijection carrying sites of the original network to sites of the relabelled network. 

### `Network.Iso.edge`

 Bijection carrying individual wires to the relabelled wires, including parallel wires. 

### `Network.Iso.payload`

 For each original wire, a bijection from its payload alphabet to the alphabet of its
  image wire. 

### `pullHalf`

 Pull a half-wire assignment at an image site back to its original site. 

### `pull`

 Pull every site's independent half-wire assignment back along the isomorphism. 

### `coeff_pull`

 The network equality tensor is invariant under the relabelling. 

### `Term.reindex`

 Transport the placements and local kernels of one term along input and output
network isomorphisms. 

### `Term.value_reindex`

 Transport preserves a term's value on the corresponding half-wire assignment. 

### `Step.reindex`

 Transport an exact step along an input network isomorphism and one output
network isomorphism for each choice. 
