---
{
  "module": "OAI/Computability/VPVNP/PairVertexReturns.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexReturns.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexReturns.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Exact consumption of the final vertex call through the histogram flush 

### `counters_terminal`

 The word-arithmetic counter loop terminates even when an arbitrary
incoming private address wraps at the word boundary. The public count is
one word, and the loop advances the external cursor exactly that many times. 

### `flush_terminal`

 Flush terminality uses no validity premise for the incoming private
memory. This supplies the arbitrary-configuration terminal case of the
DFS equivalence, as well as the case of a successfully prepared histogram. 

### `site_returns`

 The assembled per-site control returns exactly on those streams
accepted by the ordered role visits, with the empty suffix at the flush. 
