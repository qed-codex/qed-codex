---
{
  "module": "src/Main.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Codex (GPT-6.2 Astra)",
  "kind": "ai",
  "origin": "generated",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "license": "CC-BY-4.0"
}
---

# How one half-plane result supplies the five exports

AI drafted this autoinformalization from the original source. It is open for mathematical review.

Start with the third declaration. Its entire term is `New.grh`. Given a point to the right of real part $1/2$, this term supplies nonvanishing of the Dirichlet L-function for any positive modulus, subject to the condition $χ\ne1$ or $s\ne1$. The first and fourth declarations pass the same term to different lemmas. The second and fifth reuse results already named in this file. [The export terms](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Main.lean#L4-L22) · [Half-plane statement](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Statements.lean#L6-L8)

## Where the half-plane input comes from

At the end of `OneSidedBound.lean`, `New.grh` separates the point $ρ=1$ and invokes an existing nonvanishing result there. In the remaining case it chooses a real $β$ strictly between $1/2$ and $\operatorname{Re}(ρ)$. A bound on the prime remainder feeds a criterion for the character induced to modulus $18480q$, where $q$ is the original modulus. Changing the level back expresses that nonzero value as a product. Its original L-value must therefore be nonzero. [The split and intermediate exponent](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/OneSidedBound.lean#L237-L248) · [The criterion and return to the original character](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/OneSidedBound.lean#L249-L267)

## Why reflection puts a zero on the line

For the fourth export, let $s$ be a zero of $L(χ,\cdot)$ in the open critical strip. The lemma `New.zeros_on_line` rules out a vanishing gamma factor at $s$ and obtains a zero for the inverse character at $1-s$. Both points differ from $1$. Applying the half-plane input to each zero gives two inequalities, $\operatorname{Re}(s)\le1/2$ and $1-\operatorname{Re}(s)\le1/2$. Their only common solution is $\operatorname{Re}(s)=1/2$. The fifth export applies this all-character result to the supplied modulus and character. Its function body can ignore the extra witness of primitivity. [Reflection and the two inequalities](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Main.lean#L25-L42) · [Fourth and fifth exports](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Main.lean#L15-L22)

For the first export the zero is a zeta zero, which need not be given in the open strip. The lemma excludes $s=0$ using the value of zeta at zero. Together with the exclusion of the negative even integers, that gives a nonzero real gamma factor at $s$. The zero passes to completed zeta, whose reflection gives a zeta zero at $1-s$. At modulus one the half-plane result applies to zeta itself. The argument uses $s\ne1$ at the first zero and $s\ne0$ to ensure $1-s\ne1$ at the reflected zero. The same pair of inequalities now places the original zero on the critical line. The second export uses `riemannHypothesis` directly for the explicitly worded zeta statement. [Passing to completed zeta and reflecting](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Main.lean#L44-L59) · [Modulus one and the point exclusions](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Main.lean#L60-L65) · [The two zeta exports](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Main.lean#L4-L8)

I read the export file, its proposition definitions, both reflection arguments and the final derivation of `New.grh`. I did not trace the earlier prime-remainder estimate through its dependencies, or build or replay the Lean project.
