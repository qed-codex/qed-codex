---
{
  "module": "OAI/Computability/VPVNP/RankQueryDescribeSpace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryDescribeSpace.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryDescribeSpace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Independent time and space bounds for the Schur description action 

### `CallSpace`

 A local call's per-port peak as a function of the initial height. 

### `peakWith`

 Bound on each stack during description from initial height `A`. The local coefficient call
uses `peak` after the descriptor program, with additional room for clearing, copying and
writing a literal. 

### `space`

 Peak stack height for a Schur description with signed Gram entries, using `A` for initial
height and `S` for each matrix-entry read. 

### `describe_entries_bounded`

 A Schur action shares the input bank's height bound across long matrix
reads. The three-bit dispatch and the one-bit Gram tag restore their inputs. 
