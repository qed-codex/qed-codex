---
{
  "module": "OAI/Computability/VPVNP/PrimedCounterTranscriptCount.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterTranscriptCount.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterTranscriptCount.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The auxiliary RAM transcript computes the primed coefficient

The prescribed header is a word-valued function of site address. The
transcript validators first initialize RAM from that function. Their joint
path count, including all guesses at the auxiliary sites, is exactly the
grammar multiplicity for the original two groups and their exterior bits.


### `transcript_count`

 Capped auxiliary paths on the standard initialized header count the
multiplicity used in the grammar diagonal. 

### `incident_count`

 The product of the actual auxiliary validators' path counts, summed
over their shared-bit assignments, is the nominated integer coefficient. 
