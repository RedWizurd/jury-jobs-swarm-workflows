# jury-jobs-swarm-workflows

Implements agentic workflows: sequential jury runs, scheduled jobs, and tool-orchestrated swarm/Agent0 execution modes.

## Purpose
Provide reusable orchestration patterns for multi-step agent workflows where consensus, scheduling, and parallel execution are first-class.

## Features
- Sequential jury runs (`/jury`) for consensus-driven outputs.
- Job scheduling (`/jobs`) for recurring and delayed execution.
- Swarm orchestration for parallel and tree workflows.
- Agent0-dominant mode for tool control and retry logic.
- Workflow tracing and outcome capture.

## Config
- `JURY_CONFIG_PATH`: Jury participant/model configuration file.
- `JOBS_CONFIG_PATH`: Job schedule and task definitions.
- `SWARM_MAX_DEPTH`: Tree execution depth guardrail.
- `SWARM_MAX_FANOUT`: Parallel fan-out guardrail.
- `AGENT0_DOMINANT_MODE`: Enable Agent0 control over tool flow/retries.

## Quickstart
```bash
cp jury.example.json jury.json
cp jobs.example.json jobs.json
python3 scheduler.py --jobs jobs.json
python3 run_jury.py --config jury.json --task "evaluate proposals"
```

## Usage
```bash
make setup
make check
make run
```

## Roadmap
- Add workflow DSL for jury/jobs/swarm composition.
- Add per-stage retry policies and circuit breakers.
- Add execution simulator for dry runs.
- Add workflow metrics dashboards and alerts.
