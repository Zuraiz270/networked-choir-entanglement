import { useEffect, useRef, useState } from "react";
import * as d3 from "d3";
import type { InfluenceGraphResponse, GraphEdge, GraphNode } from "../types";

interface Props {
  videoId: string | null;
}

interface SimNode extends GraphNode, d3.SimulationNodeDatum {}
interface SimLink extends d3.SimulationLinkDatum<SimNode> {
  weight: number;
  lag: number;
}

const SECTION_COLOR: Record<string, string> = {
  S: "#d62728", A: "#ff7f0e", T: "#2ca02c", B: "#1f77b4",
};

export default function GraphPanel({ videoId }: Props) {
  const svgRef = useRef<SVGSVGElement | null>(null);
  const [graph, setGraph] = useState<InfluenceGraphResponse | null>(null);

  useEffect(() => {
    if (!videoId) return;
    fetch(`/api/influence_graph/${videoId}`)
      .then((r) => r.json())
      .then((data: InfluenceGraphResponse) => setGraph(data))
      .catch(() => setGraph(null));
  }, [videoId]);

  useEffect(() => {
    if (!graph || !svgRef.current) return;
    const svg = d3.select(svgRef.current);
    svg.selectAll("*").remove();
    const width = svgRef.current.clientWidth;
    const height = svgRef.current.clientHeight;

    const nodes: SimNode[] = graph.nodes.map((n) => ({ ...n }));
    const links: SimLink[] = graph.edges.map((e: GraphEdge) => ({
      source: e.source, target: e.target, weight: e.weight, lag: e.lag,
    }));

    const sim = d3
      .forceSimulation<SimNode>(nodes)
      .force("link", d3.forceLink<SimNode, SimLink>(links).id((d) => d.id).distance(80))
      .force("charge", d3.forceManyBody().strength(-200))
      .force("center", d3.forceCenter(width / 2, height / 2));

    const link = svg
      .append("g")
      .attr("stroke", "#64748b")
      .attr("stroke-opacity", 0.6)
      .selectAll<SVGLineElement, SimLink>("line")
      .data(links)
      .join("line")
      .attr("stroke-width", (d) => 0.5 + 0.4 * d.weight);

    const node = svg
      .append("g")
      .selectAll<SVGCircleElement, SimNode>("circle")
      .data(nodes)
      .join("circle")
      .attr("r", 14)
      .attr("fill", (d) => SECTION_COLOR[d.section[0]] ?? "#888")
      .attr("stroke", "#0f172a")
      .attr("stroke-width", 1.5);

    const label = svg
      .append("g")
      .selectAll<SVGTextElement, SimNode>("text")
      .data(nodes)
      .join("text")
      .text((d) => d.label)
      .attr("text-anchor", "middle")
      .attr("dy", "0.32em")
      .attr("fill", "white")
      .attr("font-size", 11)
      .attr("font-weight", "bold");

    sim.on("tick", () => {
      link
        .attr("x1", (d) => (d.source as SimNode).x ?? 0)
        .attr("y1", (d) => (d.source as SimNode).y ?? 0)
        .attr("x2", (d) => (d.target as SimNode).x ?? 0)
        .attr("y2", (d) => (d.target as SimNode).y ?? 0);
      node.attr("cx", (d) => d.x ?? 0).attr("cy", (d) => d.y ?? 0);
      label.attr("x", (d) => d.x ?? 0).attr("y", (d) => d.y ?? 0);
    });
  }, [graph]);

  return (
    <div className="flex flex-col rounded bg-slate-800 p-3">
      <h2 className="mb-2 text-sm font-semibold text-slate-300">
        Influence graph (Hacker flagship)
      </h2>
      <svg ref={svgRef} className="flex-1 rounded bg-slate-900" />
    </div>
  );
}
