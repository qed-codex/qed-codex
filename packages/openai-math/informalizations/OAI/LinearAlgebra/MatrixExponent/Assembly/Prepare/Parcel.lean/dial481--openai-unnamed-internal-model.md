---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Assembly/Prepare/Parcel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Assembly/Prepare/Parcel.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Assembly/Prepare/Parcel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Real and padding bits of a directed bundle

Additional bits are fixed to zero at both ends. They form at most
one extra span for each ordered pair of stations.



# Recognizing a parallel bundle at either endpoint

Both local patterns see the same set of ordered pairs of span
indices, counted once per wire. They can agree on one pair to carry
an extra padding span without inspecting any long host names.


 # A bijection between padding ends and their local span addresses 


# Padding a local pattern

A second copy of the span indices holds the extra bits. The label
and navigation records do not change, only the decoder.


 # Presenting the padded diagram on the original navigation network 


# Short records for a group of stations

A record contains the old labels, the bin numbers, and remote
addresses expressed relative to the child host. Bin zero holds the
exterior identities. A row with bin number zero is inactive.

