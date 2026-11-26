---
{
  "module": "src/Formalism/MeanHeightDescent/DivisionInequalityWithCovolume.lean",
  "declarations": [
    "Formalism.ExtensionFiltration.descentSlope",
    "Formalism.ExtensionFiltration.spanMuMin"
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

## Slope inequality for an injective integral map

[Theorem ARAK.1545](https://andrewodesky.com/rh/lean/Formalism.ExtensionFiltration.descentSlope/)

Let $K$ be a totally complex number field equipped with a ring involution, and let $V,W$ be finite-dimensional $K$-spaces with chosen bases. At every infinite place $v$, choose invertible complex matrices $X_v,X'_v$ defining their Hermitian norms. Let $A\subseteq V$, $B\subseteq W$ be finitely generated $\mathcal O_K$-submodules, with $A\ne0$, and let $\varphi:V\to W$ be injective and $K$-linear with $\varphi(A)\subseteq B$. Put $r_A=\dim_K KA$, $r_B=\dim_K KB$ and $$h(\varphi)=\frac1{r_\infty}\sum_{v\mid\infty}\log\|\varphi\|_v^2,\qquad r_\infty=\#\{v\mid\infty\}.$$ For an integral module $L$ in one of these metrized spaces, put $\mu(L)=2s(L)-\log2+[K:\mathbb Q]^{-1}\log|\operatorname{disc}K|$, where $s(L)$ is minus the logarithm of its Euclidean covolume divided by its $\mathbb Z$-rank; define $\mu_{\min}(L)$ by replacing $s$ with the infimum of these slopes on nonzero saturated quotients, using quotient metrics. Then $$r_A\bigl(\mu(A)-h(\varphi)\bigr)+(r_B-r_A)\mu_{\min}(B)\le r_B\mu(B).$$

## A lower bound for the minimal slope from short spanning vectors

[Theorem ARAK.1593](https://andrewodesky.com/rh/lean/Formalism.ExtensionFiltration.spanMuMin/)

Let $K$ be a totally complex number field with a chosen involution, and $V$ a finite-dimensional $K$-vector space with compatible $\mathcal O_K$-module structure. Choose a $K$-basis $b$ and invertible complex matrices $X_v$ at the infinite places, with chosen embeddings $\sigma_v:K\hookrightarrow\mathbb C$. Put $$\|x\|_v=\|X_v^{-1}\sigma_v([x]_b)\|_2,\qquad\iota(x)=(X_v^{-1}\sigma_v([x]_b))_v.$$ For a nonzero finitely generated $\mathcal O_K$-submodule $B\subseteq V$, define $$\mu_{\min}(B)=\inf_{N\subsetneq B\text{ saturated}}\frac{-\log\operatorname{covol}(\operatorname{proj}_{(\operatorname{span}_{\mathbb R}\iota(N))^\perp}\iota(B))}{\operatorname{rank}_{\mathbb Z}(B/N)},$$ where $N$ runs over $\mathcal O_K$-submodules saturated in the real span, and all covolumes use the Euclidean product norm on $\prod_v\mathbb C^{\dim_KV}$. Define $$\widetilde\mu_{\min}(B)=2\mu_{\min}(B)-\log2+\frac{\log|\operatorname{disc}K|}{[K:\mathbb Q]}.$$ If there is $S\subseteq B$ whose $K$-span contains $B$ and such that $\|x\|_v\le e^\Lambda$ for every $x\in S$ and every $v$, with $\Lambda\in\mathbb R$, then $$\widetilde\mu_{\min}(B)\ge-2\Lambda.$$
