---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/FrobeniusMatrixCofactorEqQPowFrame.lean",
  "declarations": [
    "GlobalTheory.WachPlace.FrameHeight.frame_height"
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

## A right-multiple bound for the Frobenius matrices of a Wach frame

[Theorem PHT.1044](https://andrewodesky.com/rh/lean/GlobalTheory.WachPlace.FrameHeight.frame_height/)

Retain the source's full arithmetic datum and its chosen Fontaine, Wach, and comparison data. Let $\ell$ be an odd prime, let $K/\mathbb Q_\ell$ be an unramified finite extension, and let $L/\mathbb Q_\ell$ be a finite extension in the fixed algebraic closure containing the images of every $\mathbb Q_\ell$-embedding of $K(\mu_\ell)$. Put $O=\mathcal O_L$, $f=[K:\mathbb Q_\ell]$, and let $T$ be a $G_K$-stable $O$-lattice in a crystalline $L$-representation, with labelled Hodge jumps $U_i$ for $i\in\mathbb Z/f\mathbb Z$. Suppose every jump lies in $[0,h]$.

Choose $\gamma$ in the corresponding cyclotomic group and a basis $b_1,\ldots,b_n$ of the Wach lattice over $\prod_{i\in\mathbb Z/f\mathbb Z}O[[X]]$, fixed by the finite cyclotomic subgroup. Suppose a frame is given by $P_i,D_i\in M_n(O[[X]])$ and $\Theta_i\in M_n(O)$, meaning that Frobenius and $\gamma$ have matrices $P_i(\Pi(X))$ and $(I_n+XD_i)(\Pi(X))$ in this basis, respectively, and $$(X-\ell)\mid (D_i)_{ac}-(\Theta_i)_{ac}\qquad(i,a,c).$$ Then for every $i$ there is $Q_i\in M_n(O[[X]])$ with $$P_i(\Pi(X))Q_i=q(X)^hI_n.$$
