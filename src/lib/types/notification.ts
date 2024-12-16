export enum NotificationStatus {
  Default = "default",
  Primary = "primary",
  Danger = "danger",
}

export enum NotificationPosition {
  TopLeft = "top-left",
  TopCenter = "top-center",
  TopRight = "top-right",
  BottomLeft = "bottom-left",
  BottomCenter = "bottom-center",
  BottomRight = "bottom-right",
}

export interface NotificationOptions {
  message: string;
  status?: NotificationStatus;
  timeout?: number;
  group?: string;
  pos?: NotificationPosition;
}

export interface NotificationStore {
  id: string;
  options: NotificationOptions;
}
