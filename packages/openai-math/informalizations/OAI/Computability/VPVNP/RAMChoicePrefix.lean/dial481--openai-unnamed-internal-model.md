---
{
  "module": "OAI/Computability/VPVNP/RAMChoicePrefix.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMChoicePrefix.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMChoicePrefix.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact choice streams of a burst RAM call

From fixed control and external memory, two successful streams of choices
cannot properly extend one another. The assertion is independent of their
instruction fuel. In particular, success on every bit pattern of a given
width determines the complete set of admissible streams.


### `execute_prefix_unique`

 A successful stream has no successful proper extension, even with a
different fuel allowance. Equality of streams forces equality of reports. 

### `execute_length_of_complete`

 If all length-`k` bit patterns return, every returning execution consumes
exactly `k` choices. Shorter patterns extend to length `k`, and longer patterns
have a prefix of that length. 

### `exists_execute_iff_length`

 At a fixed fuel budget, sufficiency of all fixed-width tapes also proves
necessity of that width. 
