---
{
  "module": "src/Main.lean",
  "declarations": [
    "riemannHypothesis",
    "riemannZeta_eq_zero_re",
    "LFunction_ne_zero_of_half_lt_re",
    "LFunction_eq_zero_re",
    "LFunction_eq_zero_re_of_isPrimitive"
  ],
  "author": "dial481",
  "writer": "Codex (GPT-6.2 Astra)",
  "kind": "ai",
  "origin": "generated",
  "source_commit": "40e56bab026552e089d7afcfeff08d2defb9c005",
  "license": "CC-BY-4.0"
}
---

# Main.lean and the two sides of the critical line

Take a zero of a Dirichlet $L$-function inside the open strip $0<\operatorname{Re}s<1$. To prove that it lies on the critical line, it suffices to rule out a zero on either side. The input that `Main.lean` inherits already rules out the right side for every character. A reflection argument makes the left side accessible to that same input. This distinction explains why the file can export both a nonvanishing theorem and a theorem locating zeros. [The exports](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Main.lean#L4-L12) · [The proof by position in the strip](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/CharacterBoxes/ClaimStrip.lean#L59-L73)

## The common input

`allChi` is another name for `UpperTheory.FinalTheorems.everyCharacter`. Fix a positive modulus $N$, a Dirichlet character $\chi$ modulo $N$, and a complex number $s$ with $\operatorname{Re}s>1/2$. The claim is $L(\chi,s)\ne0$ if $\chi$ is nontrivial or $s\ne1$. Thus the conclusion applies at $s=1$ for a nontrivial character. The pair consisting of the trivial character and $s=1$ is excluded. This is the theorem exported as `LFunction_ne_zero_of_half_lt_re`. [The input](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Supplements/Kernels/MainTheorems.lean#L7) · [The hypotheses](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Statements.lean#L6-L8) · [The export](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Main.lean#L8)

## Following a zero through the strip

For `LFunction_eq_zero_re`, start with an arbitrary character. If $\operatorname{Re}s>1/2$, apply the input directly, since the open strip ensures $s\ne1$. If $\operatorname{Re}s=1/2$, the assertion already holds. In the remaining case, the proof transfers the zero to the primitive character $\psi$ inducing $\chi$. Changing the level introduces a finite product. Each factor $1-\psi(p)p^{-s}$ is nonzero because $|\psi(p)|\le1$ and $|p^{-s}|<1$ for a prime $p$ and $\operatorname{Re}s>0$. Thus the product cannot account for the original zero. [The three cases](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/CharacterBoxes/ClaimStrip.lean#L59-L73) · [The individual factor](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/CharacterBoxes/ClaimStrip.lean#L7-L21) · [Transfer to the conductor](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/CharacterBoxes/ClaimStrip.lean#L23-L33)

The functional equation for the completed primitive $L$-function now gives a zero for $\psi^{-1}$ at $1-s$. Here $\operatorname{Re}(1-s)>1/2$ and $1-s\ne1$, contrary to `allChi`. The general strip theorem is the middle member of the conjunction `claimAll`. For `LFunction_eq_zero_re_of_isPrimitive`, the character is primitive from the outset and `critAll` uses the reflection directly. Both exports locate a zero conditional on its existence. [Reflection](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/CharacterBoxes/ClaimStrip.lean#L42-L57) · [The contradiction](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/CharacterBoxes/ClaimStrip.lean#L64-L73) · [The two proof terms](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Supplements/Kernels/MainTheorems.lean#L11-L16) · [The primitive case](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/GammaFactorNonvanishing/CritLine.lean#L11-L27)

## Why there are two zeta exports

`riemannHypothesis` has Mathlib's type, and `riemannZeta_eq_zero_re` has the project's spelling of it. Both exclude $s=1$ and the negative even integers, and both use the very same proof term, `rhOfAll`. Specializing `allChi` to the character modulo one gives zeta nonvanishing to the right of the line away from $1$. On the left, the functional equation introduces a cosine factor. A zero of that factor would force a negative even integer or $s=0$ in this half-plane. The hypothesis excludes the negative even integers, and the known nonzero value of zeta at zero rules out $s=0$. On the right, $s\ne1$ is the hypothesis needed to apply the nonvanishing input. Its conclusion ranges over complex zeros satisfying those exclusions, without the open-strip hypothesis of the two Dirichlet zero-location statements. [The two exports](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Main.lean#L4-L6) · [Mathlib's definition](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/NumberTheory/LSeries/RiemannZeta.lean#L182-L186) · [The project's definition](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Statements.lean#L3-L4) · [The modulus-one specialization](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/GammaFactorNonvanishing/CritLine.lean#L29-L32) · [The zeta argument](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/GammaFactorNonvanishing/RhOfRight.lean#L5-L62)
