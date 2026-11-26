---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FoundationProofs/BranchesAlongOfIrreducible.lean",
  "declarations": [
    "GlobalTheory.Branching.branchesAlong_all"
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

## Highest-weight branching rule

[Theorem ALG.0104](https://andrewodesky.com/rh/lean/GlobalTheory.Branching.branchesAlong_all/)

Let $n\ge0$ be an integer and put $N=n+1$. Let $V_\lambda$ be the irreducible rational representation of $\mathrm{GL}_N(\mathbb C)$ with dominant integral highest weight $\lambda$. For the upper-left block inclusion $\mathrm{GL}_n\hookrightarrow\mathrm{GL}_N$, $$V_\lambda\big|_{\mathrm{GL}_n}\simeq\bigoplus_{\lambda_i\ge\mu_i\ge\lambda_{i+1}}V_\mu.$$ Here the sum runs over dominant integral $n$-tuples $\mu$, and $V_\mu$ is the irreducible representation of highest weight $\mu$. Each summand occurs once. Weights failing these inequalities occur with multiplicity zero. The same assertions hold for restriction along $U(n)\hookrightarrow U(N)$. At rank zero, weights are empty tuples.
