---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsCrystallineCharJumpOne.lean",
  "declarations": [
    "GlobalTheory.LTChar.exists_crystalline_char_jump_one"
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

## A crystalline character with one prescribed weight

[Theorem PHT.1083](https://andrewodesky.com/rh/lean/GlobalTheory.LTChar.exists_crystalline_char_jump_one/)

Let $\ell\ne2$ be prime, and choose local crystalline, de Rham and integral period data, identified with Fontaine's period rings as in ([Crystallinity of a codimension-one extension and a period coboundary](https://andrewodesky.com/rh/lean/GlobalTheory.CrysExtCrit.coboundary_iff_isCrys/)) and specified below. Let $K,L\subseteq\overline{\mathbb Q}_\ell$ be finite extensions of $\mathbb Q_\ell$, with $K$ unramified, $K\subseteq K(\mu_\ell)$, and with $L$ containing every $\mathbb Q_\ell$-embedding of $K(\mu_\ell)$ into $\overline{\mathbb Q}_\ell$. For every $\tau_0:K\hookrightarrow L$ there exists a character $$\chi:G_K\to\mathcal O_L^\times$$ whose composite with $\mathcal O_L^\times\hookrightarrow L$ is continuous, whose one-dimensional $L$-representation is crystalline, and whose filtration-jump multiplicities satisfy $$m_\tau(b)=\begin{cases}1&b=1\text{ and }\tau=\tau_0,\\1&b=0\text{ and }\tau\ne\tau_0,\\0&\text{otherwise}.\end{cases}$$
