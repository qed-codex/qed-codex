---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/PiCongrRightSingle.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.OmKun.omKun"
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

## Differential forms on a tensor product of algebras

[Theorem ALG.1138](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.OmKun.omKun/)

Let $K$ be a field, let $A,B$ be commutative $K$-algebras, and let $c\ge0$. Write $\Omega^a_{A/K}=\bigwedge_A^a\Omega^1_{A/K}$. There is a $K$-linear isomorphism $$\bigoplus_{a=0}^{c}\bigl(\Omega^a_{A/K}\otimes_K\Omega^{c-a}_{B/K}\bigr)\simeq\Omega^c_{(A\otimes_KB)/K}$$ that sends the element of the $a$th summand $$(g_0\,dg_1\wedge\cdots\wedge dg_a)\otimes(h_0\,dh_1\wedge\cdots\wedge dh_{c-a})$$ to $$(g_0\otimes h_0)\,d(g_1\otimes1)\wedge\cdots\wedge d(g_a\otimes1)\wedge d(1\otimes h_1)\wedge\cdots\wedge d(1\otimes h_{c-a}).$$
