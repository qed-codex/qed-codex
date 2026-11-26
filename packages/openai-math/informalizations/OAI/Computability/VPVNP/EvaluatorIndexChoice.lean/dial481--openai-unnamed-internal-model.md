---
{
  "module": "OAI/Computability/VPVNP/EvaluatorIndexChoice.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorIndexChoice.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorIndexChoice.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A binary machine choice below an input bound

The evaluator guesses a basis index after each linear step. It also makes a
final choice below the prime-field residue. This finite-control routine consumes
the little-endian bits of the bound and guesses one bit for each. Comparing
successive, more significant bits requires only one bit of state. A successful
choice writes the guessed bits in big-endian order onto the output stack.


### `Phase`

 Finite control for a bounded binary guess. It retains the comparison with the bound as it
reads and writes successive bits. 

### `guessBelow`

 Each bit takes a pop, a two-way choice and a push. A final pop and
comparison either return to the continuation or halt in rejection. 

### `written`

 Replace the exhausted bound by the empty stack and prepend the guessed
bits, high bit first, to the destination. 

### `count_guessBelow`

 The continuation runs once per legal binary representation, at exactly
the same remaining fuel on all successful branches. 

### `count_guessBelow_fin`

 With a bound encoded as one word, the integer count is the sum over the
legal index type. There are no duplicate representations or modulo aliases. 

### `count_final_residue`

 Returning with one successful leaf per legal final guess realizes the
representative of the prime-field residue as an integer path count. 

### `allStops_guessBelow`

 Every nonrejecting branch returns a legal ordinal with the same residual
clock, while every illegal choice has already halted. 

### `guessBelow_stops`

 Even illegal index guesses halt within the same linear instruction clock. 

### `final_residue_paths`

 Close the returning routine as an accepting machine: its actual binary
branch tree has exactly the specified number of accepting leaves. 
