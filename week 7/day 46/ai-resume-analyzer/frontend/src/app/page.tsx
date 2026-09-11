"use client";

import {
  type ChangeEvent,
  type DragEvent,
  type ReactNode,
  useId,
  useRef,
  useState,
} from "react";

const API_BASE =
  process.env.NEXT_PUBLIC_API_URL?.replace(/\/$/, "") || "http://127.0.0.1:8000";

type DocMode = "pdf" | "text";
type RequirementStatus = "strong_match" | "partial" | "missing";

type RequirementMatch = {
  requirement: string;
  status: RequirementStatus;
  evidence: string | null;
  gap: string | null;
};

type AnalysisResult = {
  candidate_name: string;
  matched_skills: string[];
  missing_skills: string[];
  strengths: string[];
  weaknesses: string[];
  match_score: number;
  recommendation: string;
  requirement_match_breakdown?: RequirementMatch[];
};

const MIN_TEXT_CHARS = 20;

export default function Home() {
  const [resumeMode, setResumeMode] = useState<DocMode>("pdf");
  const [resumeFile, setResumeFile] = useState<File | null>(null);
  const [resumeText, setResumeText] = useState("");

  const [jobMode, setJobMode] = useState<DocMode>("pdf");
  const [jobFile, setJobFile] = useState<File | null>(null);
  const [jobText, setJobText] = useState("");

  const [result, setResult] = useState<AnalysisResult | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const resumeReady =
    resumeMode === "pdf"
      ? Boolean(resumeFile)
      : resumeText.trim().length >= MIN_TEXT_CHARS;
  const jobReady =
    jobMode === "pdf"
      ? Boolean(jobFile)
      : jobText.trim().length >= MIN_TEXT_CHARS;
  const canAnalyze = resumeReady && jobReady && !loading;

  const analyzeResume = async () => {
    if (!resumeReady || !jobReady) {
      setError(
        "Please provide both the resume and the job description, as a PDF or pasted text."
      );
      return;
    }

    setError("");
    setLoading(true);
    setResult(null);

    try {
      const form = new FormData();
      if (resumeMode === "pdf" && resumeFile) {
        form.append("resume", resumeFile);
      } else {
        form.append("resume_text", resumeText.trim());
      }
      if (jobMode === "pdf" && jobFile) {
        form.append("job_description", jobFile);
      } else {
        form.append("job_description_text", jobText.trim());
      }

      const response = await fetch(`${API_BASE}/analyze-mixed`, {
        method: "POST",
        body: form,
      });

      let data: unknown = null;
      try {
        data = await response.json();
      } catch {
        // Response body wasn't valid JSON; handled below.
      }

      if (!response.ok) {
        const detail =
          data && typeof data === "object" && "detail" in data
            ? String((data as { detail?: unknown }).detail)
            : `Analysis failed (${response.status}).`;
        throw new Error(detail);
      }

      if (!data || typeof data !== "object") {
        throw new Error("Received an unexpected response from the server.");
      }

      setResult(data as AnalysisResult);
    } catch (caughtError) {
      if (caughtError instanceof TypeError) {
        setError(
          "Could not reach the analysis server. Make sure the backend is running at " +
            API_BASE +
            "."
        );
      } else {
        setError(
          caughtError instanceof Error
            ? caughtError.message
            : "Something went wrong. Please try again."
        );
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen bg-background text-foreground">
      <div className="mx-auto w-full max-w-[1240px] px-5 pb-20 pt-6 sm:px-8 lg:px-10">
        <header className="grid grid-cols-[minmax(0,1fr)_auto] items-center gap-4 border-b border-border pb-5">
          <div className="flex min-w-0 items-center gap-3">
            <span
              className="grid size-9 shrink-0 place-items-center rounded-md border border-border bg-surface"
              aria-hidden="true"
            >
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img src="/logo.png" alt="" className="size-6 object-contain" />
            </span>
            <span className="truncate text-[15px] font-semibold">
              Fitscope - AI Resume Analyzer
            </span>
          </div>
          <span className="shrink-0 rounded-full border border-border px-2.5 py-1 font-mono text-[10px] uppercase text-muted-foreground">
            ATS Review
          </span>
        </header>

        <section className="pb-9 pt-12 sm:pb-12 sm:pt-16">
          <p className="mb-4 font-mono text-[11px] uppercase text-accent">
            Compatibility workspace
          </p>
          <h1 className="max-w-3xl text-4xl font-semibold leading-[1.08] sm:text-5xl lg:text-[58px]">
            A clearer view of your fit for the role.
          </h1>
          <p className="mt-5 max-w-2xl text-base leading-7 text-muted-foreground">
            Provide your resume and the job description — each as a PDF or
            pasted text, in any combination — to compare your experience
            against the role, identify meaningful gaps, and focus your next
            revision.
          </p>
        </section>

        <section
          aria-label="Documents"
          className="grid gap-px overflow-hidden rounded-lg border border-border bg-border lg:grid-cols-2"
        >
          <DocumentPanel
            number="01"
            title="Resume"
            description="Your current resume or CV"
            mode={resumeMode}
            onModeChange={setResumeMode}
            file={resumeFile}
            onFileChange={setResumeFile}
            text={resumeText}
            onTextChange={setResumeText}
          />
          <DocumentPanel
            number="02"
            title="Job Description"
            description="The role you are targeting"
            mode={jobMode}
            onModeChange={setJobMode}
            file={jobFile}
            onFileChange={setJobFile}
            text={jobText}
            onTextChange={setJobText}
          />
        </section>

        <div className="mt-10 flex flex-col items-center gap-4 text-center">
          <p className="max-w-md text-xs leading-5 text-faint">
            {resumeReady && jobReady
              ? "Both documents are ready for analysis."
              : "Provide each document as a PDF with selectable text, or paste the text directly — mixing formats is fine."}
          </p>

          <button
            type="button"
            onClick={analyzeResume}
            disabled={!canAnalyze}
            className="inline-flex h-14 items-center justify-center gap-2.5 rounded-md bg-accent px-10 text-sm font-semibold text-accent-foreground transition-colors hover:bg-accent-muted focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent disabled:cursor-not-allowed disabled:opacity-50"
          >
            {loading ? (
              <>
                <Spinner />
                Analyzing…
              </>
            ) : (
              <>
                <AnalyzeMark />
                Analyze compatibility
              </>
            )}
          </button>
        </div>

        {error && (
          <div
            role="alert"
            className="mt-5 flex items-start gap-3 rounded-md border border-error-border bg-error-surface p-4 text-sm leading-6 text-error-strong"
          >
            <AlertMark />
            <p>{error}</p>
          </div>
        )}

        {result && <Results result={result} />}
      </div>
    </main>
  );
}

function DocumentPanel({
  number,
  title,
  description,
  mode,
  onModeChange,
  file,
  onFileChange,
  text,
  onTextChange,
}: {
  number: string;
  title: string;
  description: string;
  mode: DocMode;
  onModeChange: (mode: DocMode) => void;
  file: File | null;
  onFileChange: (file: File | null) => void;
  text: string;
  onTextChange: (text: string) => void;
}) {
  const inputId = useId();
  const inputRef = useRef<HTMLInputElement>(null);
  const [dragging, setDragging] = useState(false);
  const [fileError, setFileError] = useState("");

  const chooseFile = (nextFile?: File) => {
    if (!nextFile) return;
    if (
      nextFile.type !== "application/pdf" &&
      !nextFile.name.toLowerCase().endsWith(".pdf")
    ) {
      setFileError("Choose a PDF file.");
      return;
    }
    setFileError("");
    onFileChange(nextFile);
  };

  const handleInput = (event: ChangeEvent<HTMLInputElement>) =>
    chooseFile(event.target.files?.[0]);

  const handleDrop = (event: DragEvent<HTMLDivElement>) => {
    event.preventDefault();
    setDragging(false);
    chooseFile(event.dataTransfer.files?.[0]);
  };

  const removeFile = () => {
    onFileChange(null);
    setFileError("");
    if (inputRef.current) inputRef.current.value = "";
  };

  return (
    <article className="min-w-0 bg-surface p-5 sm:p-7">
      <div className="grid grid-cols-[minmax(0,1fr)_auto] items-start gap-4">
        <div className="min-w-0">
          <div className="flex min-w-0 items-center gap-3">
            <span className="font-mono text-[11px] text-accent">{number}</span>
            <h2 className="truncate text-lg font-semibold">{title}</h2>
          </div>
          <p className="mt-1 pl-8 text-sm text-muted-foreground">
            {description}
          </p>
        </div>

        <div className="inline-flex shrink-0 rounded-full border border-border p-0.5 font-mono text-[10px] uppercase">
          <button
            type="button"
            onClick={() => onModeChange("pdf")}
            aria-pressed={mode === "pdf"}
            className={`rounded-full px-2.5 py-1 transition-colors focus-visible:outline-2 focus-visible:outline-accent ${
              mode === "pdf"
                ? "bg-accent text-accent-foreground"
                : "text-muted-foreground hover:text-foreground"
            }`}
          >
            PDF
          </button>
          <button
            type="button"
            onClick={() => onModeChange("text")}
            aria-pressed={mode === "text"}
            className={`rounded-full px-2.5 py-1 transition-colors focus-visible:outline-2 focus-visible:outline-accent ${
              mode === "text"
                ? "bg-accent text-accent-foreground"
                : "text-muted-foreground hover:text-foreground"
            }`}
          >
            Text
          </button>
        </div>
      </div>

      {mode === "pdf" ? (
        <div
          onDragEnter={(event) => {
            event.preventDefault();
            setDragging(true);
          }}
          onDragOver={(event) => event.preventDefault()}
          onDragLeave={() => setDragging(false)}
          onDrop={handleDrop}
          className={`mt-6 rounded-md border border-dashed p-4 transition-colors ${
            dragging
              ? "border-accent bg-accent-subtle"
              : "border-border-strong bg-panel"
          }`}
        >
          <input
            ref={inputRef}
            id={inputId}
            type="file"
            accept="application/pdf,.pdf"
            onChange={handleInput}
            className="sr-only"
          />
          {file ? (
            <div className="grid grid-cols-[auto_minmax(0,1fr)_auto] items-center gap-3">
              <span className="grid size-10 shrink-0 place-items-center rounded-md border border-border bg-surface text-accent">
                <PdfMark />
              </span>
              <div className="min-w-0">
                <p className="truncate text-sm font-medium">{file.name}</p>
                <p className="mt-0.5 font-mono text-[10px] uppercase text-muted-foreground">
                  PDF · {formatFileSize(file.size)} · Ready
                </p>
              </div>
              <div className="flex shrink-0 items-center gap-1">
                <button
                  type="button"
                  onClick={() => inputRef.current?.click()}
                  className="rounded px-2 py-1 text-xs font-medium text-muted-foreground hover:bg-muted hover:text-foreground focus-visible:outline-2 focus-visible:outline-accent"
                >
                  Replace
                </button>
                <button
                  type="button"
                  onClick={removeFile}
                  className="grid size-7 place-items-center rounded text-muted-foreground hover:bg-muted hover:text-foreground focus-visible:outline-2 focus-visible:outline-accent"
                  aria-label={`Remove ${title} file`}
                  title="Remove file"
                >
                  <CloseMark />
                </button>
              </div>
            </div>
          ) : (
            <label
              htmlFor={inputId}
              className="flex cursor-pointer flex-col items-center px-3 py-4 text-center focus-within:outline-2 focus-within:outline-accent"
            >
              <span className="grid size-10 place-items-center text-muted-foreground">
                <UploadMark />
              </span>
              <span className="mt-2 text-sm font-medium">
                Drop a PDF here or <span className="text-accent">browse</span>
              </span>
              <span className="mt-1 text-xs text-faint">
                PDF with selectable text
              </span>
            </label>
          )}
        </div>
      ) : (
        <div className="mt-6">
          <label className="sr-only" htmlFor={`${inputId}-text`}>
            {title} text
          </label>
          <textarea
            id={`${inputId}-text`}
            value={text}
            onChange={(event) => onTextChange(event.target.value)}
            placeholder={`Paste the ${title.toLowerCase()} text here…`}
            className="min-h-40 w-full resize-y rounded-md border border-border-strong bg-panel px-4 py-3.5 text-sm leading-6 text-foreground outline-none placeholder:text-faint focus:border-accent focus:ring-1 focus:ring-accent"
          />
          <div className="mt-2 flex items-center justify-between font-mono text-[10px] uppercase text-faint">
            <span>
              {text.trim().length >= MIN_TEXT_CHARS
                ? "Text provided"
                : "Awaiting content"}
            </span>
            <span>{text.length.toLocaleString()} chars</span>
          </div>
        </div>
      )}
      {mode === "pdf" && fileError && (
        <p className="mt-2 text-xs text-error">{fileError}</p>
      )}
    </article>
  );
}

function Results({ result }: { result: AnalysisResult }) {
  const breakdown = result.requirement_match_breakdown ?? [];
  const score = Math.min(100, Math.max(0, result.match_score ?? 0));

  return (
    <section
      className="mt-16 border-t border-border pt-10"
      aria-labelledby="results-heading"
    >
      <div className="mb-7 flex flex-col gap-2 sm:flex-row sm:items-end sm:justify-between">
        <div>
          <p className="font-mono text-[11px] uppercase text-accent">
            Analysis complete
          </p>
          <h2
            id="results-heading"
            className="mt-2 text-2xl font-semibold sm:text-3xl"
          >
            Compatibility report
          </h2>
        </div>
        <p className="text-sm text-muted-foreground">
          Candidate:{" "}
          <span className="font-medium text-foreground">
            {result.candidate_name || "Unknown"}
          </span>
        </p>
      </div>

      <div className="grid overflow-hidden rounded-lg border border-border bg-border lg:grid-cols-[0.72fr_1.28fr] lg:gap-px">
        <div className="bg-surface p-6 sm:p-8">
          <p className="font-mono text-[10px] uppercase text-muted-foreground">
            Overall match
          </p>
          <div className="mt-5 flex items-end gap-1">
            <strong className="text-6xl font-semibold leading-none sm:text-7xl">
              {score}
            </strong>
            <span className="pb-1 text-2xl text-muted-foreground">%</span>
          </div>
          <div className="mt-7 h-1.5 overflow-hidden rounded-full bg-muted">
            <div
              className="h-full rounded-full bg-accent"
              style={{ width: `${score}%` }}
            />
          </div>
          <p className="mt-3 text-xs text-faint">
            Resume-to-role compatibility
          </p>
        </div>
        <div className="border-t border-border bg-surface p-6 sm:p-8 lg:border-l lg:border-t-0">
          <p className="font-mono text-[10px] uppercase text-muted-foreground">
            Recommendation
          </p>
          <p className="mt-5 max-w-2xl text-base leading-7 text-secondary-foreground">
            {result.recommendation || "No recommendation available."}
          </p>
        </div>
      </div>

      <div className="mt-px grid gap-px overflow-hidden rounded-lg border border-border bg-border sm:grid-cols-2">
        <ResultSection
          title="Matched skills"
          items={result.matched_skills}
          tone="positive"
        />
        <ResultSection
          title="Missing skills"
          items={result.missing_skills}
          tone="warning"
        />
        <ResultSection
          title="Strengths"
          items={result.strengths}
          tone="neutral"
        />
        <ResultSection
          title="Weaknesses"
          items={result.weaknesses}
          tone="neutral"
        />
      </div>

      <RequirementBreakdown breakdown={breakdown} />
    </section>
  );
}

function ResultSection({
  title,
  items,
  tone,
}: {
  title: string;
  items: string[];
  tone: "positive" | "warning" | "neutral";
}) {
  const safeItems = items ?? [];
  const marker =
    tone === "positive"
      ? "bg-success"
      : tone === "warning"
        ? "bg-warning"
        : "bg-accent-muted";
  return (
    <article className="bg-surface p-6 sm:p-7">
      <div className="flex items-center justify-between gap-3">
        <h3 className="text-sm font-semibold">{title}</h3>
        <span className="font-mono text-[10px] text-faint">
          {safeItems.length.toString().padStart(2, "0")}
        </span>
      </div>
      {safeItems.length ? (
        <ul className="mt-5 space-y-3">
          {safeItems.map((item, index) => (
            <li
              key={`${item}-${index}`}
              className="grid grid-cols-[auto_1fr] gap-3 text-sm leading-6 text-muted-foreground"
            >
              <span
                className={`mt-2.5 size-1.5 rounded-full ${marker}`}
                aria-hidden="true"
              />
              <span>{item}</span>
            </li>
          ))}
        </ul>
      ) : (
        <p className="mt-5 text-sm text-faint">No items identified.</p>
      )}
    </article>
  );
}

const STATUS_LABEL: Record<RequirementStatus, string> = {
  strong_match: "Strong match",
  partial: "Partial",
  missing: "Missing",
};

const STATUS_DOT: Record<RequirementStatus, string> = {
  strong_match: "bg-success",
  partial: "bg-warning",
  missing: "bg-error",
};

function RequirementBreakdown({
  breakdown,
}: {
  breakdown: RequirementMatch[];
}) {
  const counts = {
    strong_match: breakdown.filter((r) => r.status === "strong_match").length,
    partial: breakdown.filter((r) => r.status === "partial").length,
    missing: breakdown.filter((r) => r.status === "missing").length,
  };

  return (
    <div className="mt-10">
      <div className="mb-5 flex flex-col gap-2 sm:flex-row sm:items-end sm:justify-between">
        <h3 className="text-xl font-semibold">Requirement match breakdown</h3>
        {breakdown.length > 0 && (
          <div className="flex flex-wrap items-center gap-4 font-mono text-[11px] uppercase text-muted-foreground">
            <CountPill
              label="Strong"
              count={counts.strong_match}
              dot="bg-success"
            />
            <CountPill label="Partial" count={counts.partial} dot="bg-warning" />
            <CountPill label="Missing" count={counts.missing} dot="bg-error" />
          </div>
        )}
      </div>

      {breakdown.length === 0 ? (
        <div className="rounded-lg border border-border bg-surface p-6 text-sm text-faint">
          No requirement breakdown was returned for this analysis.
        </div>
      ) : (
        <ul className="divide-y divide-border overflow-hidden rounded-lg border border-border bg-surface">
          {breakdown.map((item, index) => (
            <li key={`${item.requirement}-${index}`} className="p-5 sm:p-6">
              <div className="flex flex-wrap items-start justify-between gap-3">
                <p className="max-w-2xl text-sm font-medium leading-6">
                  {item.requirement}
                </p>
                <span className="inline-flex shrink-0 items-center gap-2 rounded-full border border-border px-2.5 py-1 font-mono text-[10px] uppercase text-muted-foreground">
                  <span
                    className={`size-1.5 rounded-full ${STATUS_DOT[item.status]}`}
                    aria-hidden="true"
                  />
                  {STATUS_LABEL[item.status] ?? item.status}
                </span>
              </div>

              {item.evidence && (
                <p className="mt-3 text-sm leading-6 text-muted-foreground">
                  <span className="text-faint">Evidence — </span>
                  {item.evidence}
                </p>
              )}

              {item.gap && (
                <p className="mt-2 text-sm leading-6 text-muted-foreground">
                  <span className="text-faint">Gap — </span>
                  {item.gap}
                </p>
              )}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

function CountPill({
  label,
  count,
  dot,
}: {
  label: string;
  count: number;
  dot: string;
}) {
  return (
    <span className="inline-flex items-center gap-1.5">
      <span className={`size-1.5 rounded-full ${dot}`} aria-hidden="true" />
      {label} {count.toString().padStart(2, "0")}
    </span>
  );
}

function formatFileSize(bytes: number) {
  if (bytes < 1024 * 1024) return `${Math.max(1, Math.round(bytes / 1024))} KB`;
  return `${(bytes / (1024 * 1024)).toFixed(1)} MB`;
}

function Icon({
  children,
  className = "size-5",
}: {
  children: ReactNode;
  className?: string;
}) {
  return (
    <svg
      className={className}
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="1.7"
      strokeLinecap="round"
      strokeLinejoin="round"
      aria-hidden="true"
    >
      {children}
    </svg>
  );
}

const PdfMark = () => (
  <Icon>
    <path d="M7 2.8h7l3.2 3.2v15.2H7z" />
    <path d="M14 2.8V6h3.2M9.5 15.5h5M9.5 12.5h3" />
  </Icon>
);
const UploadMark = () => (
  <Icon className="size-6">
    <path d="M12 16V4M8 8l4-4 4 4M5 15v4h14v-4" />
  </Icon>
);
const AnalyzeMark = () => (
  <Icon>
    <path d="M4 6h16M4 12h10M4 18h7" />
    <path d="m17 15 3 3-3 3" />
  </Icon>
);
const AlertMark = () => (
  <Icon className="mt-0.5 size-4 shrink-0">
    <path d="M12 8v5M12 17h.01" />
    <path d="M10.3 3.7 2.6 17a2 2 0 0 0 1.7 3h15.4a2 2 0 0 0 1.7-3L13.7 3.7a2 2 0 0 0-3.4 0Z" />
  </Icon>
);
const CloseMark = () => (
  <Icon className="size-4">
    <path d="m7 7 10 10M17 7 7 17" />
  </Icon>
);
const Spinner = () => (
  <span
    className="size-4 animate-spin rounded-full border-2 border-current border-t-transparent motion-reduce:animate-none"
    aria-hidden="true"
  />
);
