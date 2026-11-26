---
{
  "module": "OAI/Computability/VPVNP/ExpanderOrders.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ExpanderOrders.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ExpanderOrders.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Arbitrarily large dyadic graph orders

Section 5.3 of *VP and VNP differ over every field* iterates a fixed port graph
and then removes loops by doubling. A real line in the target class forces
each resulting multigraph to be connected.


### `exists_expander_orders`

 A port graph of dyadic order and degree yields connected, loopless
multigraphs of unbounded dyadic order, with one degree and one Poincaré
bound for all orders and targets. 
