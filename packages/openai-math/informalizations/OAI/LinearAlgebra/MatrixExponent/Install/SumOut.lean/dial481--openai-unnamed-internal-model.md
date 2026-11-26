---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Install/SumOut.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Install/SumOut.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Install/SumOut.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Packing whole fibres into bins of twice the average capacity 

 # Pushing a weighted network through deterministic postprocessing 

 # Summing a weight over hidden indices 

 # Running a finite family of circuits on shared input bits 


# Assigning endpoint records to batches

Compute a bucket mask for each batch and look up the mask bit at
each endpoint's source. The batch is active if the mask is nonempty.
The lookup works for repeated source identifiers.



# Grouped transports before batching

The count and width of candidate groups may depend on the fixed
height ratio. The total width actually used must have a uniform bound.


### `GroupProtocol`

 Configurable core transports in fixed groups, with endpoint
payloads padded to a common chunk length. 


# Sizing the installation

The slack in each group is one batch. Choosing its exponent below the
group height absorbs the excess candidate capacity. Rounding the total
installed width to a power of two costs a factor at most two.


 # Converting bounded groups into candidate batches 


# Cost of distributing the transports

The distribution cost can depend on the excess capacity `B`, which
is fixed before the height tends to infinity. The coefficient in the
bound on installed payload is independent of `B`.

