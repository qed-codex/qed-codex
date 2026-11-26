---
{
  "module": "src/Formalism/FormalGroupWitt/FormalGroupWittProofs/SolveV.lean",
  "declarations": [
    "Formalism.FG.solve_exists_vector"
  ],
  "author": "dial481",
  "writer": "Andrew O'Desky",
  "origin": "other-author",
  "source": "https://andrewodesky.com/rh/",
  "source_commit": "40e56bab026552e089d7afcfeff08d2defb9c005",
  "license": "with-permission"
}
---

As published on 26 November 2026.

## Solving a multivariable formal substitution equation

[Theorem ALG.0245](https://andrewodesky.com/rh/lean/Formalism.FG.solve_exists_vector/)

Let $R$ be a commutative ring, and let $I,J$ be finite sets. For $i\in I$, let $f_i\in R[[X_k:k\in I]]$ and $G_i\in R[[Y_j:j\in J]]$. Assume $$f_i(0)=0,\qquad [X_k]f_i=\delta_{ik},\qquad G_i(0)=0.$$ There exist series $h_i\in R[[Y_j:j\in J]]$ with $h_i(0)=0$ such that $$f_i((h_k)_{k\in I})=G_i\qquad(i\in I).$$
