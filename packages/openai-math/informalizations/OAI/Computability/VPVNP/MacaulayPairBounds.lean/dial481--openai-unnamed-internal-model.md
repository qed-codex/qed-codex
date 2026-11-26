---
{
  "module": "OAI/Computability/VPVNP/MacaulayPairBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayPairBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayPairBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Uniform register widths and bounds for the physical Macaulay entry arms

The actual physical clocks in the two returning routines are singly
exponential. Their stack bounds are polynomial in the arity, register width
and caller's live stack bound, independently of the size of the index scan.


### `requiredWidth`

 Common register width accommodating both graded-key scans, the optional coordinate shift
and the scaled exponent comparisons. 

### `fits_of_width`

 One advised register width works for every pair of legal ordinals at
these degrees, including the shifted power comparison. 

### `resources`

 The bounds of the actual two binary controls under the bit-size
hypotheses of Lemma 8.2. Both include advice staging and final cleanup. 
