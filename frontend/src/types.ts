export interface VideoMeta {
  video_id: string;
  title: string;
  regime: string;
  n_singers: number;
  duration_s: number;
}

export interface EntanglementSeries {
  time_sec: number[];
  A: number[];
  V: number[];
  N: number[];
  E: number[];
}

export interface EntanglementResponse {
  video_id: string;
  window_sec: number;
  step_sec: number;
  series: EntanglementSeries;
}

export interface GraphNode {
  id: string;
  label: string;
  section: string;
}

export interface GraphEdge {
  source: string;
  target: string;
  weight: number;
  lag: number;
}

export interface InfluenceGraphResponse {
  video_id: string;
  nodes: GraphNode[];
  edges: GraphEdge[];
}
