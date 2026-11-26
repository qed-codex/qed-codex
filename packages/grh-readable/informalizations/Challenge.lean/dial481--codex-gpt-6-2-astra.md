---
{
  "module": "Challenge.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Codex (GPT-6.2 Astra)",
  "kind": "ai",
  "origin": "generated",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "license": "CC-BY-4.0"
}
---

# Which zeros do the five challenge declarations cover?

AI drafted this autoinformalization from the original source. It is open for mathematical review.

The easiest way to read this file is to ask what information is given about a complex number $s$. One target starts with its position and rules out a zero. The others start with a zero and constrain its position. Each of the five declarations has a `sorry` body here. Comparator lists their names and pairs the challenge module with the solution module `Main`. [The five targets](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/Challenge.lean#L3-L20) · [Comparator configuration](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/comparator.json#L2-L10)

## Starting with a point to the right

Take a positive modulus $N$, a Dirichlet character $χ$ modulo $N$, and any $s$ with $\operatorname{Re}(s)>1/2$. The third target says $L(χ,s)\ne0$ provided $χ\ne1$ or $s\ne1$. At $s=1$ this still asks for nonvanishing for every nonprincipal character. For the principal character the same target applies at every other point of that open half-plane. It gives no conclusion on the boundary itself. [Third declaration](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/Challenge.lean#L13-L14) · [Quantifiers and exception](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Statements.lean#L6-L8)

## Starting with a zero

For the zeta function, the first declaration uses Mathlib’s name `RiemannHypothesis`. The second uses the project’s spelling of the condition. Suppose $ζ(s)=0$, $s\ne1$, and $s$ is different from every number $-2(n+1)$ with $n$ a natural number. Then $\operatorname{Re}(s)=1/2$. There is no need to supply an open-strip hypothesis in this version. The solution file gives the first declaration itself as the term for the second. [Zeta targets](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/Challenge.lean#L7-L11) · [Excluded points](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Statements.lean#L3-L4) · [The connection in Main](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Main.lean#L4-L8)

The fourth target takes a different starting assumption. The input is already a zero of a Dirichlet L-function in the open strip $0<\operatorname{Re}(s)<1$. The conclusion is again $\operatorname{Re}(s)=1/2$. The fifth asks for the same conclusion when the character is primitive. For a zero with real part exactly $1$, the open-strip statements do not apply, whereas the third target still applies if its character or point condition holds. [Last two declarations](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/Challenge.lean#L16-L20) · [Half-plane and strip definitions](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Statements.lean#L6-L16)

I read the challenge, the proposition definitions, the five exports and the Comparator configuration at the linked revision. I did not run Lean or Comparator, or audit the argument supplying the five targets.
