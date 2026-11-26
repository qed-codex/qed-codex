---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Sphere/Ledger/Quota.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Sphere/Ledger/Quota.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Sphere/Ledger/Quota.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Counting linked spans and exterior pins at one station 

### `exterior_sum`

 Count exposed ends in two ways, first in diagram order and then
by the local pin numbering. 

### `arity_links`

 Each linked span contributes its full width, independently of
direction. This counts both ends of a loop at the same station. 


# The square budget after subtracting exterior wires

Rounding and routing cost at most a multiple of T/D² per
station. Squaring this error leaves an O(D T²) term even when
an occupied cell retains D⁵ frozen stations.


 # Restricting the collected energy to one occupied cell 

 # Aggregating squared collector charges in one cell 

 # Aligning live child slots with the vertices of their parent 

### `sum_child`

 A live child at these coordinates arises from exactly one vertex based
at this parent. The equality applies to weights in any additive monoid. 

 # Frozen station charges in the ordered diagram 

 # Frozen square bound for a single occupied cell 

 # Counting the internal bits displayed by a printed blueprint 

 # Maximum toll of a frozen or mobile child 

### `toll_charge`

 An unoccupied slot costs nothing. At a live slot the toll is
at most the full charge of its vertex. 

 # Translating charges between child labels and physical stations 

 # Every genuine blueprint satisfies the finite quota check 
