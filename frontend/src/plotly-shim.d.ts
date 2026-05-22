declare module "plotly.js-dist-min" {
  type PlotlyData = Record<string, unknown>;
  type PlotlyLayout = Record<string, unknown>;
  type PlotlyConfig = Record<string, unknown>;

  function react(
    root: HTMLElement,
    data: PlotlyData[],
    layout?: PlotlyLayout,
    config?: PlotlyConfig,
  ): Promise<void>;
  function newPlot(
    root: HTMLElement,
    data: PlotlyData[],
    layout?: PlotlyLayout,
    config?: PlotlyConfig,
  ): Promise<void>;
  function purge(root: HTMLElement): void;

  const _default: { react: typeof react; newPlot: typeof newPlot; purge: typeof purge };
  export default _default;
}
