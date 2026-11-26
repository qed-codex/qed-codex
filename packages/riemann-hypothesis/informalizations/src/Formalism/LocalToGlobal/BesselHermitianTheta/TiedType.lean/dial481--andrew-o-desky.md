---
{
  "module": "src/Formalism/LocalToGlobal/BesselHermitianTheta/TiedType.lean",
  "declarations": [
    "Formalism.L2.Theta.TypTied"
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

## Smooth automorphic functions and discrete-series types

[Definition / hypothesis ARAK.D233](https://andrewodesky.com/rh/lean/Formalism.L2.Theta.ThetaSmoothnessCondition/)

Use ([Automorphic theta functions and their measures](https://andrewodesky.com/rh/lean/Formalism.L2.Theta.ThetaTied/)) and the smooth automorphic functions, Lie derivatives, finite-dimensional infinitesimal-character condition and common polynomial growth exponent defined in ([Analytic realizations of rational Hecke families](https://andrewodesky.com/rh/lean/Formalism.IndefR.Links.RealDat.BaseW/)). Use the Hilbert discrete-series models, lowest compact weights and conjugated coordinate actions defined in ([Analytic and rational realization data](https://andrewodesky.com/rh/lean/Formalism.IndefR.Links.RealDat/)). Fix any compatible infinite embedding family. For a matrix $g$ at one place, $g_\tau$ below denotes a selected purely infinite adelic lift with identity components elsewhere, if one exists, and the identity otherwise.

Hypothesis (smooth theta realization). For every Hermitian space with correct Gram signatures, the image of $e_V$ is exactly the smooth automorphic functions just defined. This assertion holds for every compatible infinite embedding family, and at least one such family exists.

Here is the precise local type criterion. For a finite set $S\subset\mathbb Q\times\{+,-\}$, enumerate it as $(\lambda_a,\epsilon_a)_{0\le a<n}$ with strictly decreasing rational $\lambda_a$. Choose a discrete-series model $\sigma$ on a nonzero Hilbert space $H$, for sign matrix $J_\epsilon$ and parameter $\lambda$, and an invertible $P$ with $P^*J_\epsilon P=G_{V,\tau}$. Put $\sigma_P(g)=\sigma(PgP^{-1})$. A smooth vector means that its orbit under every finite product $\prod_i\exp(t_iX_i)$ is smooth, with $X_i^*G_{V,\tau}+G_{V,\tau}X_i=0$. For a finite list $\mathcal D$ of words in this real Lie algebra, put $p_{\mathcal D}(v)=\sum_{D\in\mathcal D}\|d\sigma_P(D)v\|$, using iterated derivatives at zero and the identity for an empty word. A complex-linear functional on $H$ is Sobolev bounded if $|\ell(v)|\le C p_{\mathcal D}(v)$ for all smooth $v$, for some finite $\mathcal D$ and real $C$.

Say a scalar function $f$ has local type $S$ if such $H,\sigma,\lambda,\epsilon,P$ exist and the following holds at every adelic base point $x$. There are smooth vectors $v_i$, Sobolev bounded linear functionals $\ell_i$, one common finite Lie-word list $\mathcal D$ and real bounds $C_i$ such that $$|\ell_i(v)|\le C_i p_{\mathcal D}(v)$$ for all smooth $v$, and $\sum_i C_i p_{\mathcal D'}(v_i)$ is summable for every finite Lie-word list $\mathcal D'$. There is a continuous real function $B$ on all complex matrices with $$p_{\mathcal D}(\sigma_P(g)v)\le B(g)p_{\mathcal D}(v)$$ for every unitary $g$ and smooth $v$. For every such $g$, the series converges with the indicated value: $$f(xg_\tau)=\sum_{i=0}^\infty\ell_i(\sigma_P(g)v_i).$$ The model and $P$ are chosen once for $S,\tau,f$; the sequences, list and bounds may depend on $x$.

Hypothesis (theta type comparison). Let $V$ have rank $n$ and correct signature $(p_\tau,q_\tau)$. At each $\tau$, let $S_\tau$ admit a strictly decreasing rational enumeration with $p_\tau$ positive and $q_\tau$ negative signs and $\lambda_a-(n-1)/2\in\mathbb Z$. If $p_\tau q_\tau\ne0$, require there to be a real $h>\max(2n,8n\min(p_\tau,q_\tau))$ such that every pair in $S_\tau$ with different signs has parameter distance at least $h$. Then, for every $F\in\mathcal A(V)$, $$F\in\mathcal A(V)[(S_\tau)_\tau]\quad\Longleftrightarrow\quad e_VF\text{ has local type }S_\tau\text{ at every }\tau.$$ The left side denotes the prescribed type subspace in ([Hermitian theta spaces and pairings](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.ThetaX/)). This equivalence holds for every compatible infinite embedding family; those families exist.
