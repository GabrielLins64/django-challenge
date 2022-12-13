export interface User {
  id: number;
  username: string;
  email: string;
  is_staff: boolean;
  is_active: boolean;
}

export type Token = string;

export interface Vulnerability {
  id: number;
  asset_hostname: string;
  asset_ip_address: string;
  title: string;
  severity: string;
  cvss: number | null;
  publication_date: Date | null;
  fixed: boolean;
}

export interface ListResponse {
  count: number;
  next: string | null;
  previous: string | null;
  results: Array<any>;
}
