---
{
  "module": "src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/PlaceSplit.lean",
  "declarations": [
    "Formalism.HN.PlaceDecomposition.finrank_span_complex"
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

## Ranks of real and complex lattice realizations

[Theorem ARAK.0149](https://andrewodesky.com/rh/lean/Formalism.HN.place_lattice_structure/)

Let $K$ be a number field equipped with an involution, $n=[K:\mathbb Q]$, $\Delta_K=\operatorname{disc}K$, and $\Sigma_\infty(K)$ its set of infinite places, of cardinality $t$. Let $V$ be a finite-dimensional $K$-space, equipped with the induced $\mathcal O_K$-action, and choose a basis $b$. For each infinite place $v$ choose a representing embedding $\sigma_v:K\to\mathbb C$ and an invertible complex matrix $X(v)$ of size $\dim_KV$. For $x\in V$ set $$f_v(x)=X(v)^{-1}\sigma_v([x]_b),\qquad\rho(x)=\bigl(\Re f_v(x),\Im f_v(x)\bigr)_{v\in\Sigma_\infty(K)},$$ where the target of $\rho$ has its Euclidean norm and $\sigma_v$ acts coordinatewise.

For every finitely generated $\mathcal O_K$-submodule $L\subseteq V$, the map $\rho$ is injective on $L$, its image is discrete, and, writing $k=\dim_K\operatorname{span}_K L$, $$\operatorname{rk}_{\mathbb Z}\rho(L)=nk,\qquad 2^{tk}|\Delta_K|^{-k/2}\operatorname{covol}_{\mathbb R}\rho(L)>0.$$ Covolume is taken in the real span of the image. If $K$ is totally complex, then for every $\mathcal O_K$-submodule $A\subseteq V$, without a finite generation hypothesis, and every infinite place $v$, $$\dim_{\mathbb C}\operatorname{span}_{\mathbb C}f_v(A)=\dim_K\operatorname{span}_K A.$$
