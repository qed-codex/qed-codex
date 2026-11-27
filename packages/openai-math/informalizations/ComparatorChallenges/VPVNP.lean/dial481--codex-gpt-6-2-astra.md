---
{
  "module": "ComparatorChallenges/VPVNP.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Codex (GPT-6.2 Astra)",
  "kind": "ai",
  "origin": "generated",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "license": "CC-BY-4.0"
}
---

# Two predicates on the same polynomial families

AI drafted this autoinformalization from the original source. It is open for mathematical review.

Fix a field $F$. At index $n$, the theorem uses polynomials with variables labelled by `Fin n × Bool`: each of the $n$ positions supplies two variable labels. On families with these variables the theorem asks for inequality of the predicates `IsVP` and `IsVNP`. It quantifies over every field. The body here is the challenge placeholder `sorry`. [VPVNP.lean lines 24–36](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/VPVNP.lean#L24-L36) · [VPVNP.lean lines 47–55](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/VPVNP.lean#L47-L55)

What does it cost to compute a polynomial? An instruction takes two available polynomials and adds, subtracts or multiplies them. Constants and input variables are available from the start. Each subsequent instruction may reuse any earlier result, including the same operand twice. An output need only be available at the end. A family belongs to VP if its variable count, total degree and required number of instructions have eventual polynomial bounds in $n$. [VPVNP.lean lines 11–22](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/VPVNP.lean#L11-L22) · [VPVNP.lean lines 27–36](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/VPVNP.lean#L27-L36)

VNP keeps the variable-count and degree bounds. It allows a larger VP polynomial with extra witness variables, polynomially many in $n$. Assign those variables all possible Boolean values, evaluate them as zero or one in $F$, and add the resulting polynomials. The sum must equal the original polynomial at each index. This sum lies in the polynomial ring over $F$. Different witness assignments can contribute to the same coefficient. [VPVNP.lean lines 38–43](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/VPVNP.lean#L38-L43)

I read the challenge file at this revision. I did not build the project or check a construction separating the predicates.
