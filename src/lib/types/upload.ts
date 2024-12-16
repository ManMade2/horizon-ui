export interface UploadOptions {
	url: string;
	multiple?: boolean;
	name?: string;
	params?: Record<string, any>;
	allow?: string;
	mime?: string;
	onBeforeSend?: (environment: any) => void;
	onProgress?: (event: ProgressEvent) => void;
	onComplete?: (e: any) => void;
	onError?: (error: any) => void;
}

export interface UploadProps {
	options: UploadOptions;
	dragAndDrop?: boolean;
	buttonLabel?: string;
	dropzoneText?: string;
}
