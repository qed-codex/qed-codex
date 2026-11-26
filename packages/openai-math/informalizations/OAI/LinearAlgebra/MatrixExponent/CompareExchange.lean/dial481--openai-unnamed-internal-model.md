---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/CompareExchange.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/CompareExchange.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/CompareExchange.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A linear-size compare-and-exchange network on words

Comparison folds a single bit of state up the word. Selection copies that bit
to all positions, then multiplexes them in parallel. This avoids paying for
identity on a shrinking word at each step of a sequential selection.


### `wordOrder`

 Lexicographic order with the first bit most significant. 

### `ternary`

 Evaluate both two-input branches and select with the third bit. 

### `compare_lt`

 A strict comparator using a linear number of trivalent vertices. 

### `compare_exchange`

 Order the two words while retaining both of them. 
