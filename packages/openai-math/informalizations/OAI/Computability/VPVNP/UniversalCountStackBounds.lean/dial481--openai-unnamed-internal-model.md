---
{
  "module": "OAI/Computability/VPVNP/UniversalCountStackBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/UniversalCountStackBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/UniversalCountStackBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Time and space for the witness enumerator

For a verifier using at most `B` steps per witness, the counter makes exactly
one call per binary word. The bound on the height of every stack is independent
of the number of calls. This follows by restarting the space estimate at each
call boundary, where the counters have their original widths and the auxiliary
stacks have their original contents.


### `SpaceRun`

 Every stack in every intermediate configuration has length at most `cap`. 

### `digits`

 The low `w` bits in the same order as the finite Boolean witness. 

### `testAt`

 Applies the witness predicate to the low w bits of the given index in little-endian order. 

### `enumerate_runs`

 A full run returns the numeric count in a `w + 1` bit register. The
control remains fixed across word lengths and verifier inputs. Each individual
stack stays within the stated space bound throughout the run. 
