---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/ModuliProofs/ExistsThetaFrameFamily.lean",
  "declarations": [
    "GlobalTheory.exists_thetaFrame_family"
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

## A constant half-characteristic for a connected family of theta frames

[Theorem AV.0800](https://andrewodesky.com/rh/lean/GlobalTheory.exists_thetaFrame_family/)

Assume the polarized abelian-scheme laws specified in the conventions below and the uniformization assertion ([Theta functions for a principally polarized complex abelian variety](https://andrewodesky.com/rh/lean/GlobalTheory.thetaUnifAV_closed/)). Fix CM moduli data, with the host and polarized-lattice conventions of ([An indefinite polarized CM lattice splits by signature](https://andrewodesky.com/rh/lean/GlobalTheory.T.hermitianLatticeSignatureSplit_of_indefinite/)), field $E$, signature $(p,q)$ with $p+q\ge1$, level data, universal polarized abelian scheme $(\mathcal A,L)$ and the specified compatible complex embedding. Choose embeddings $\phi_1,\ldots,\phi_g:E\hookrightarrow\mathbb C$ with the prescribed CM multiplicities. Choose a second polarized lattice datum $(\Lambda,E_\Lambda)$ in the same system and an $\mathcal O_E$-linear map from the original moduli lattice to $\Lambda$.

Let $B\subset\mathbb C^m$ be open and preconnected. Suppose $y:B\to X(\mathbb C)$ and $e_b:\mathbb C^g\to\mathcal A_{y(b)}(\mathbb C)$ are holomorphic, the latter jointly in $(b,z)$. Assume each $y(b)$ lies over the specified embedding, $e_b$ is a surjective group homomorphism inducing an isomorphism on tangent spaces, and $\ker e_b=P_b(\Lambda)$, where $P_b:\Lambda\to\mathbb C^g$ is an injective period map with discrete full real span. Require $P_b$ to be $\mathcal O_E$-linear for the action $\alpha(z_j)_j=(\phi_j(\alpha)z_j)_j$, with its coordinates holomorphic in $b$, and require $e_b$ to respect this action. Assume the polarization and level compatibilities below.

Choose a basis $u_1,\ldots,u_g,v_1,\ldots,v_g$ of $\Lambda$ for which $E_\Lambda$ is $\epsilon$ times the standard symplectic form, with $\epsilon=\pm1$. Suppose matrices $h_b,\tau_b\in M_g(\mathbb C)$ satisfy $$h_bP_b(u_j)=e_j,\qquad h_bP_b(v_j)=\tau_be_j,\qquad\operatorname{Im}\tau_b>0.$$ There are constant vectors $c_1,c_2\in\{0,1/2\}^g$ such that $$\vartheta_b(z)=\sum_{n\in\mathbb Z^g}\exp\left(\pi i(n+c_1)^t\tau_b(n+c_1)+2\pi i(n+c_1)^t(h_bz+c_2)\right)$$ defines a theta frame for $L$ over the whole family, in the sense below.
