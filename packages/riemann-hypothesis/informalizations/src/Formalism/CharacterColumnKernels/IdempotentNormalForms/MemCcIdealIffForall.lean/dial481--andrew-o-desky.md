---
{
  "module": "src/Formalism/CharacterColumnKernels/IdempotentNormalForms/MemCcIdealIffForall.lean",
  "declarations": [
    "Formalism.NG.vccBaseChange"
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

## Ramification scaling of an evaluation ideal

[Theorem ALG.0831](https://andrewodesky.com/rh/lean/Formalism.NG.vccBaseChange/)

Let $\mathcal O,\mathcal O'$ be discrete valuation domains, with $\mathcal O'$ a finite free $\mathcal O$-algebra. Let $e\ge0$ be an integer and assume their normalized additive valuations satisfy $$v_{\mathcal O'}(a)=e\,v_{\mathcal O}(a)\qquad(a\in\mathcal O),$$ where $a$ on the left denotes its image in $\mathcal O'$. Let $X$ be any set, let $T\subseteq\mathcal O^X$ be an $\mathcal O$-subalgebra, and let $T'\subseteq(\mathcal O')^X$ be an $\mathcal O'$-subalgebra equal to the $\mathcal O'$-linear span of the coefficientwise images of functions in $T$.

For $Z\subseteq X$ and $x\in X$, put $$c_{\mathcal O}(T,Z,x)=\inf_{\substack{f\in T\\ f|_{X\setminus Z}=0}}v_{\mathcal O}(f(x)).$$ Then $$c_{\mathcal O'}(T',Z,x)=e\,c_{\mathcal O}(T,Z,x).$$
